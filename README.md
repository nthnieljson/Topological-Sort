# Tucil-2-Stima

Algoritma yang digunakan dalam menyelesaikan permasalahan penyusunan rencana kuliah adalah algoritma topological sort. Algoritma topological sort secara singkat dapat diterapkan dengan cara memilih simpul simpul yang tidak memiliki derajat masuk pada setiap iterasinya. Algoritma topological sort juga sangatlah erat dengan konsep decrease and conquer. Proses decrease pada algoritma topological sort dapat kita lihat pada fase pemilihan simpul pada setiap iterasinya. Graph kemudian akan meng-decrease sejumlah simpul. Dapat dilihat bahwa pada setiap iterasinya, kita mengurangi input yang kita dapat, dengan tujuan untuk mencapai suatu solusi yang optimal.

# requirements

python 3.8.5

# cara menggunakan program

1. buatlah input file di folder test
2. file input dibuat dengan menggunakan format tertentu, yaitu untuk setiap mata kuliah dibatasi dengan koma, dan line diakhiri dengan titik. Sisakan 1 baris kosong pada akhir file. Contoh input dapat dilihat pada folder test
3. pastikan anda berada pada folder utama
4. lalu ketik <code>python3 src/main_13519108.py </code>
5. masukan nama file yang ingin digunakan sebagai input
