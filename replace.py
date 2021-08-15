import os

dirname = "./sea_turtle/OIDv4_ToolKit/OID/Dataset/train/Sea_turtle"
text_files = [f for f in os.listdir(dirname) if f.endswith('.txt')]
for txt_file in text_files:
    with open(os.path.join(dirname, txt_file), 'r+') as f:
        for line in f:
            line = line.rstrip()
            words = line.split(" ", maxsplit = 1)
            words[0] = '0'
            f.truncate(0)
            break
            
    with open(os.path.join(dirname, txt_file), 'w') as f:
        outfile = ' '.join(words)
        f.write(outfile)


# python3 train.py --img 600 --batch 16 --epochs 30 --data sea_turtle.yaml --cfg ./models/yolov5s.yaml --weights  '' --name yolov5s_results  --cache --device 0

