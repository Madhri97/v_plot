set terminal pngcairo size 1200,900 enhanced font "Arial,14"
set output "vplot.png"

# Set axis labels
set xlabel "Position relative to midpoint"
set ylabel "Fragment Length (bp)"
set zlabel "Count"
set title "V-Plot: Fragment Length vs Relative Position"

# Set a blue to white color palette
set palette defined (0 "white", 1 "blue")

#Customize axis ranges
set xrange [-500:500]
set yrange [0:500]


plot "vplot_data.tsv" using 1:2:(($3)) with points palette pointsize 1 title "Counts"
