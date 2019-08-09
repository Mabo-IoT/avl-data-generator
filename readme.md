## avl data generate
AVL 数据随机生成器

## Usage
```
docker-compose -f up -d   //依赖与redis
```

## Content
1. mesurement: AVL_engine_durability
2. eqpt_no: '1900'
3. data:
```
"anl_lmbdafrcfr_x": self.random_float(-1,1)，空燃比(Lambda)
"bct1_ex_t": self.random_float(20, 630),三元催化前温度
"bskl_air_t": self.random_float(20,25),环境温度
"bskl_cba_ap": self.random_float(10,11),大气压力
"cac_airi_ap": self.random_float(96, 101),中冷前压力
"cac_airi_t": self.random_float(20, 40),中冷前温度
"cac_airo_ap": self.random_float(95, 102),中冷后压力
"cac_airo_t": self.random_float(12, 36),中冷后温度
"cac_airt_dvl": self.random_float(34, 36),中冷温度命令值
"cbn_ve_pct": self.random_float(0, 1),充气效率
"cc_gas_p": self.random_float(-0.1, 1),曲轴箱压力
"cel_air_t": self.random_float(20, 30),进气温度
"cel_relhum_pct": self.random_float(0,1),湿度
"ct1a_ex_t": self.random_float(20, 650),三元催化后温度
"cwc_pidact_t": self.random_float(0, 100),AVL533水温
"cwc_wtrbyp_p": self.random_float(1, 90),小循环压力
"cwc_wtrbyp_t": self.random_float(20, 95),小循环温度
"cwc_wtri_p": self.random_float(0, 100),进水压力
"cwc_wtri_t": self.random_float(0,100),进水温度
"cwc_wtro_p": self.random_float(0, 100),出水压力
"cwc_wtro_t": self.random_float(0, 100),出水温度
"cwc_wtro_dvl": self.random_float(0, 100),冷却液温度命令值
"d_afil_tq": self.random_float(0,150),测功机扭矩
"d_spddig_n": self.random_float(0, 5000),测功机转速
"e_bmep_P": self.random_float(0, 10),BMEP
"e_edsp_vl": self.random_float(0, 65),发动机排量
"e_obsfc_fe": self.random_float(0, 10),比油耗
"e_pwr_pw": self.random_float(0, 10),发动机功率
"e_saeapp_tq": self.random_float(-100000, 0),修正扭矩
"ecol_res_p": self.random_float(0, 100),水箱压力
"eo_cool_vf": self.random_float(20, 70),冷却液流量
"esp_oil_t": self.random_float(20,110),油底壳温度
"ex_bkpvlvr_set": self.random_float(0, 5),背压命令值
"ex_postctbk_p": self.random_float(-2, 2),三元催化后压力
"ex_prectbk_p": self.random_float(0, 18),三元催化前压力
"f_f_dox": self.random_float(0, 2),汽油密度
"fl_sup_p": self.random_float(0, 400),燃油压力
"oc_eoilt_dvl": self.random_float(0, 100),机油温度命令值
"oc_pidact_t": self.random_float(20, 100),机油小车温度
"og_oil_p": self.random_float(0, 260),主油道压力
"og_oil_t": self.random_float(20, 105),主油道温度
"ok_fire": random.randint(0,1),火警报警
"ok_gas": random.randint(0,1),气体报警
"s_cycdone_cnt": random.randint(0,1000),实验循环数
"s_f_t": self.random_float(0, 20),燃油温度
"s_saeapp_pw": self.random_float(-100000, 0),修正功率
"status": random.randint(0,1),实验状态
```