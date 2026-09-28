# Hardware evaluation

Applicable models: **AlohaMini 2 / 2 Pro**. Run only the example for your robot.

The evaluation script reads the policy checkpoint, generates actions based on current observations, and saves the evaluation data. **The commands in this chapter will control the real robot.** First confirm that teleoperation is normal, and then use matching data, models and models to evaluate.

## 1. Preparation before assessment

1. Start the correct model of Host on the Pi.
2. Stop teleoperation, recording and other command clients to release control.
3. Check which robot, camera configuration and task the policy comes from.
4. Confirm that the checkpoint directory actually exists and that the files are complete.
5. Prepare a new `dataset.repo_id` for this evaluation and set the scene starting state.
6. Maintain an operating position where you can end the program promptly and do a small amount of testing first.

## 2. ACT Simultaneous Assessment

**AlohaMini 2**

```bash
python examples/alohamini/evaluate_bi.py \
  --eval.n_episodes 3 \
  --fps 20 \
  --eval.episode_time_s 45 \
  --dataset.single_task "Pick up the object and place it in the tray" \
  --policy.path outputs/train/act_am2_pick_place/checkpoints/020000/pretrained_model \
  --dataset.repo_id $HF_USER/eval_act_am2_run01 \
  --dataset.push_to_hub=false \
  --robot.remote_ip <Pi_IP> \
  --robot.id my_alohamini \
  --robot.robot_model alohamini2 \
  --inference.type sync \
  --interpolation_multiplier 3
```

**AlohaMini 2 Pro**

```bash
python examples/alohamini/evaluate_bi.py \
  --eval.n_episodes 3 \
  --fps 20 \
  --eval.episode_time_s 45 \
  --dataset.single_task "Pick up the object and place it in the tray" \
  --policy.path outputs/train/act_am2pro_pick_place/checkpoints/020000/pretrained_model \
  --dataset.repo_id $HF_USER/eval_act_am2pro_run01 \
  --dataset.push_to_hub=false \
  --robot.remote_ip <Pi_IP> \
  --robot.id my_alohamini \
  --robot.robot_model alohamini2pro \
  --inference.type sync \
  --interpolation_multiplier 3
```

Replace checkpoint steps and Pi IP. `eval.n_episodes=3` is an example test number, not a guarantee of effect; follow the program prompts to reset the environment between each test.

## 3. Understand evaluation parameters

| parameters | Description |
| --- | --- |
| `eval.n_episodes` | The number of tasks for this assessment |
| `eval.episode_time_s` | Single assessment duration |
| `fps` | Target frequency of evaluation loop |
| `policy.path` | Model identifiers supported by local model directories or portals |
| `dataset.single_task` | Description of the task performed this time |
| `dataset.repo_id` | Evaluation result data set identification, separate from training data |
| `dataset.push_to_hub=false` | Keep only local assessment data |
| `robot.id` | Robot equipment identification |
| `robot.robot_model` | The robot model corresponding to the Host and model |
| `inference.type` | `sync` Synchronous inference, or policy-enabled `rtc` |
| `interpolation_multiplier` | Action interpolation multiple |

The first time a result identifier is used, the target data directory should not yet exist. The new round of experiments is changed to new names such as `run02`, and the results of the previous round are retained for comparison.

### Interpolation frequency is not equal to model inference frequency

The example of 20 Hz with 3x interpolation corresponds to outputting interpolated actions at a target 60 Hz after the first action; this does not turn the model itself into 60 inferences per second. Actual execution is also affected by inference time, network and control loops.

## 4. RTC Evaluation: Supported Policies Only

The project provides examples of policies supporting RTC interfaces such as SmolVLA. ACT does not support this RTC path, `sync` should be used.

When a compatibility policy checkpoint is in place, the relevant portion of the evaluation command can be changed to:

```text
--inference.type rtc
--inference.rtc.execution_horizon 10
--inference.rtc.max_guidance_weight 10.0
--inference.rtc.queue_threshold 30
--interpolation_multiplier 1
```

The remaining robot, model path and data set parameters still need to be passed in completely. RTC uses background inference and action queues, and the policy must provide the required action chunk interface; any model cannot be made compatible by changing parameters alone.

## 5. Feedback expires or protection is suspended

The current client requires complete feedback for issuing commands from requests sent within the last 250 ms. After synchronous inference, expired feedback is refreshed and old responses prefetched before inference are discarded.

**250 ms is the feedback freshness limit, not the time limit when model inference must be completed.** But the Host's watchdog is still in effect; watchdog events, joint protection, Host restarts, or control changes will suspend evaluation and discard the action queue until explicitly restored. The program does not bypass the watchdog via empty beats.

If you encounter a pause, first check the logs on both the Host and PC to determine whether it is an issue with time-consuming inference, network, device protection, or control rights. Don't directly increase the timeout threshold as the first step to fix it.

## 6. Record results and review

| record item | Sample content |
| --- | --- |
| Data and models | Dataset name, checkpoint, training configuration |
| Hardware | Whether the model, camera layout, and calibration have changed |
| scene | Objects, starting position, lighting and background |
| result | Whether the goal has been completed, how long it took, and manual intervention |
| failure stage | approach, grab, carry, place or end |
| Abnormal operation | Missing image, timeout, protection trigger, control change |

Try to keep the same set of scenario definitions and success criteria when comparing different checkpoints. Distinguish operational issues from policy issues before deciding to fix the configuration, supplement the demo, or retrain.
