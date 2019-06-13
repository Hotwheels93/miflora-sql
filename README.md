# miflora-sql
Python script to push data from Miflora flower care to SQL database using the library of open-homeautomation (https://github.com/open-homeautomation/miflora)

## Preperations ## 

If you havent installed miflora library, bluez and mysql-connector for python yet, follow instructions 1-4, else continue with 5.

### Install dependencies and libraries ###

### 1. Install bluez ###
> sudo apt-get update
sudo apt-get upgrade
sudo apt-get bluez

### 2. Install miflora libray ###
> sudo pip3 install miflora

### 3. Install bluepy ###
> sudo pip3 install bluepy

### 4. Install mysql-connector ###
> sudo pip3 install mysql-connector-python

### 5. Scan devices ###

> sudo hcitool lescan

##### Note the MAC adress of device "Flower care". It should look like this C4:7C:8D:xx:xx:xx #####

### 6. Clone git and config database connection ###

> git clone https://github.com/Hotwheels93/miflora-sql.git
cd miflora-sql

Open miflora-sql-update.py

#### Change: #####

- database credentials (host, user, pw, database [line 24-27])
- MAC adress [line 11] 
- device/plant name[12]

> Save and exit file

### 7. Create database tables ###

Login to your server via phpMyAdminand and import the plants.sql or create table manually

### 8. Run & autostart it ### 

sudo python3 miflora-sql-update.py 
#### sudo is needed because of system bluetooth functions ###

> sudo crontab -e

e.g. for updating every 30 minutes

> */30 * * * * sudo python3 /home/pi/miflora-sql/miflora-sql-update.py .  (change to your location)




