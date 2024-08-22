#!/bin/bash

echo "Test Started"

# CPU için stres testi. Sonsuz döngü oluşturuyor.
(while :; do :; done) &
cpu_pid=$!

# Bellek için stres testi. Belleği yaklaşık %99 seviyesinde kullanacak şekilde ayarlandı.
stress-ng --vm-bytes 99% --vm-keep -m 1 --timeout 30s &
mem_pid=$!

# Disk için stres testi. /khas dizininde toplamda 5210 kez 1 MB'lık veri (Yaklaşık 5 GB) yazılıyor.
dd if=/dev/zero of=/khas/tempfile bs=1M count=5120 conv=fdatasync &
disk_pid=$!

#30 saniye bekleme.
sleep 30

# Tüm süreçleri sonlandıran blok.
kill -9 $cpu_pid $mem_pid
kill -9 $disk_pid

# Disk üzerinde test için oluşturulan dosyayı temizleyen blok.
rm -f /khas/tempfile

echo "Test Completed"