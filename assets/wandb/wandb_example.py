import wandb


def train(learning_rate):
    config = {
        "model": "single_weight",
        "learning_rate": learning_rate,
        "epochs": 40,
        "initial_weight": 0.0,
        "target_weight": 3.0,
    }
    run = wandb.init(
        project="learning-rate-comparison",
        name=f"lr-{learning_rate}",
        config=config,
    )

    weight = config["initial_weight"]
    target = config["target_weight"]
    for epoch in range(1, config["epochs"] + 1):
        gradient = 2 * (weight - target)
        weight -= config["learning_rate"] * gradient
        loss_value = (weight - target) ** 2
        run.log(
            {
                "epoch": epoch,
                "train_loss": loss_value,
                "weight": weight,
            },
            step=epoch,
        )

    run.finish()


if __name__ == "__main__":
    wandb.login()
    for learning_rate in (0.05, 0.2):
        train(learning_rate)
