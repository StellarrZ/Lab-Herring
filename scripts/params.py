hyperparameters = {"fp16": "",
                    "task": "masked_lm",
                    "criterion": "masked_lm",
                    "arch": "roberta_large",
                    "sample-break-mode": "complete",
                    "tokens-per-sample": 512,
                    "optimizer": "adam",
                    "adam-eps": 1e-6,
                    "clip-norm": 0.0,
                    "lr-scheduler": "polynomial_decay",
                    "lr": 0.0001,
                    "warmup-updates": 200,
                    "total-num-update": 500,
                    "dropout": 0.1,
                    "attention-dropout": 0.1,
                    "weight-decay": 0.01,
                    "max-sentences": 8,
                    "update-freq": 1,
                    "max-update": 2000,
                    "log-format": "simple",
                    "log-interval": 1,
                    "encoder-layers": 24,
                    "encoder-embed-dim": 2048,
                    "encoder-ffn-embed-dim": 8192,
                    "memory-efficient-fp16": "",
                    "distributed-no-spawn" : "",
                    "skip-invalid-size-inputs-valid-test": "",
                    "disable-validation" : "",
                    "no-save": ""}


for k, v in hyperparameters.items():
    print("  --%s" % k, "%s" % v, "\\")