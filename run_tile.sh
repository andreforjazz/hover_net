python run_infer.py \
--gpu='1' \
--nr_types=0 \
--type_info_path=type_info.json \
--batch_size=64 \
--model_mode=original \
--model_path=../pretrained/hovernet_original_consep_notype_tf2pytorch.tar \
--nr_inference_workers=8 \
--nr_post_proc_workers=16 \
tile \
--input_dir=dataset/sample_tiles/imgs/ \
--output_dir=dataset/sample_tiles/pred/ \
--mem_usage=0.1 \
--draw_dot \
--save_qupath