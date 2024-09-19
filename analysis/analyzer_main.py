from loss_analyzer import LossAnalyzer

def main():
    log_file_paths = [
        "../log/log_0919_1032_57.txt",
    ]

    metrics_analyzers = [
        LossAnalyzer,
    ]

    for log_file_path in log_file_paths:
        for metrics_analyzer in metrics_analyzers:
            metrics_analyzer(log_file_path, metrics_name="g_loss").plot()

if __name__ == "__main__":
    main()
