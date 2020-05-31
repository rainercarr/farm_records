To install/run this app you need to run the following:
(in Powershell)

virtualenv farm_records
.\Scripts\activate

pip install --default_timeout=100 django==3.0.6
mkdir farm_records_src 
cd farm_records_src
git clone (this repository)
