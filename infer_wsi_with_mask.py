import os
from time import time

src = r"\\10.162.80.16\Andre\data\monkey fetus\gestational 40"
cachedir = r"C:\Users\Andre\Desktop\cache"
start = time()
dst = os.path.join(src,'hovernet_out')
maskdir = r'\\10.162.80.16\Andre\data\monkey fetus\gestational 40\20x_mask'
if not os.path.exists(dst): os.mkdir(dst)

# nr_inference_workers 0 if fails
os.system('python run_infer.py '\
          '--nr_types={} '\
          '--batch_size={} '\
          '--nr_inference_workers={} '\
          '--nr_post_proc_workers={} '\
          '--model_mode={} '\
          '--model_path={} '\
          'wsi '\
          '--input_dir="{}" '\
          '--output_dir="{}" '\
          '--proc_mag={} '\
          '--input_mask_dir="{}" '\
          '--cache_path="{}" '\
          .format(0,16,8,11,'original',
                  "./models/pretrained/hovernet_original_consep_notype_tf2pytorch.tar",
                  src,
                  dst,
                  20,
                  maskdir,
                  cachedir
                  )
          )
end = time()
print('execution time : ',end-start)

