dt=Gazette_finetune_thinkaloud
base=llava-v1.5-7b
epoch=1
export TRITON_CACHE_DIR="../triton/"

deepspeed --include="localhost:0,1" --master_port 29603 llava/train/train_mem.py \
    --deepspeed ./scripts/zero3_offload.json \
    --lora_enable True \
    --model_name_or_path liuhaotian/llava-v1.5-7b \
    --version v1 \
    --data_path ../data/training/$dt.json \
    --vision_tower openai/clip-vit-large-patch14-336 \
    --mm_projector_type mlp2x_gelu \
    --mm_vision_select_layer -2 \
    --mm_use_im_start_end False \
    --mm_use_im_patch_token False \
    --image_aspect_ratio pad \
    --group_by_modality_length True \
    --bf16 True \
    --output_dir ../checkpoints/$base-$dt-ep$epoch \
    --num_train_epochs $epoch \
    --per_device_train_batch_size 16 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 1 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 50000 \
    --save_total_limit 5 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --tf32 True \
    --model_max_length 2048 \
    --gradient_checkpointing True \
    --dataloader_num_workers 4 \
    --lazy_preprocess True
    --report_to wandb