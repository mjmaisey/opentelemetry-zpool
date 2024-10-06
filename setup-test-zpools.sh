#!/bin/sh
sudo apt-get install zfsutils-linux
sudo mkdir /var/local/zfs
sudo dd if=/dev/zero of=/var/local/zfs/test_zpool bs=1M count=128
sudo zpool create test /var/local/zfs/test_zpool
sudo dd if=/dev/zero of=/var/local/zfs/testw_zpool bs=1M count=128
sudo zpool create test2 /var/local/zfs/testw_zpool
