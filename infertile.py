import os
from time import time

src = r"\\babyserverdw5\Digital pathology image lib\L Wood\211120 PDAC fibroblast quantification\raw czi images\HE\20x\tiles"
cachedir = r"C:\Users\kyuha\Desktop\cache"
start = time()
dst = os.path.join(src,'hovernet_out')
# nr_inference_workers 0 if fails
os.system('python run_infer.py '\
          '--nr_types={} '\
          '--batch_size={} '\
          '--nr_inference_workers={} '\
          '--nr_post_proc_workers={} '\
          '--model_mode={} '\
          '--model_path={} '\
          'tile '\
          '--input_dir="{}" '\
          '--output_dir="{}" '\
          .format(0,16,8,11,'original',
                  "./models/pretrained/hovernet_original_consep_notype_tf2pytorch.tar",
                  src,
                  dst,
                  )
          )
end = time()
print('execution time : ',end-start)

