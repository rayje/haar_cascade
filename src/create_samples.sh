#! /bin/sh

NUM_IMAGES=10 # The number of sample images to create
BGCOLOR=255   # The background color that can be interpreted as a backgroud. This will be made transparent.
BGTHRESH=1    # The number added to BGCOLOR as a range to also be included as backgroud
WIDTH=50      # The width of the sample
HEIGHT=50     # The height of the sample

for i in $(cat resized_images/positives.txt); do
    part1=$(echo $i | cut -d '_' -f 3)
    if [ $part1 -eq 1 ]; then
        # Images where $part1 == 1 have fewer samples
        # than images that have $part1 == 0, so include
        # every other image.
        part=$(echo $i | cut -d '_' -f 4)
        num=$(echo $part | cut -d '.' -f 1)
        echo "part: $part1, num: $num" >> create.log
        if ! (($num % 2)); then
            echo "part: $part1, num: $num" >> create.log
            opencv_createsamples -img resized_images/$i \
                -bg negative_images/negatives.txt \
                -info samples/$(basename $i).txt \
                -num $NUM_IMAGES -maxxangle 0.3 -maxyangle 0.3 \
                -maxzangle 0.0 -bgcolor $BGCOLOR -bgthresh $BGTHRESH \
                -w $WIDTH -h $HEIGHT
            echo $i >> processed.txt
        fi
    else
        # More of these images exist, and are very similar,
        # so include every 5th image.
        part2=$(echo $i | cut -d '_' -f 4)
        num=$(echo $part2| cut -d '.' -f 1)
        if ! (($num % 5)); then
            echo "part2: $part2, num: $num" >> create.log
            opencv_createsamples -img resized_images/$i \
                -bg negative_images/negatives.txt \
                -info samples/$(basename $i).txt \
                -num $NUM_IMAGES -maxxangle 0.3 -maxyangle 0.3 \
                -maxzangle 0.0 -bgcolor $BGCOLOR -bgthresh $BGTHRESH \
                -w $WIDTH -h $HEIGHT 
            echo $i >> processed.txt
        fi
    fi
done

cd samples
cat image_*.jpg.txt > positives.txt
# Count the number of samples created
num_positives=$(wc -l positives.txt | awk '{print $1}')
cd ..

cp negative_images/negatives.txt ./bg.txt

echo "----------------------------------------"
echo " num positives: $num_positives"
echo "----------------------------------------"

opencv_createsamples -info samples/positives.txt \
    -bg bg.txt \
    -vec samples.vec \
    -num $num_positives -w 50 -h 50
