CARLA PPO Agent (Town07)

This project uses Proximal Policy Optimization (PPO) to train and evaluate autonomous driving agents in the CARLA simulator, specifically tailored for **Town07**.

## Prerequisites

- [CARLA Simulator](https://carla.org/) (recommended: version 0.9.13)
- Python 3.8+

## How to Run

1.  **Start CARLA in Low Resolution:**

    ```bash
    CarlaUE4.exe -windowed -ResX=800 -ResY=600 -quality-level=Low
    ```

2.  **Run a Pretrained Agent (carla_ppo_10):**

    * download the carla_ppo_10 model from drive link and store it in Carla-ppo\models
    * In a new terminal, run:

    ```bash
    python run_eval.py --model_name carla_ppo_10
    ```

3.  **Train a New PPO Agent:**

    ```bash
    python train.py --model_name carla_ppo_model
    ```

4. Pretrained agent drive link : https://drive.google.com/drive/folders/1gKMpTcX9-2ETuSbCwXuBTUwnDzhqXH3T?usp=sharing
