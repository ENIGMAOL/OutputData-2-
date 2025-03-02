#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  appDhtWebServer.py
#  
#  Created by MJRoBot.org 
#  10Jan18

'''
	RPi Web Server for DHT captured data  
'''

from flask import Flask, render_template, request
app = Flask(__name__)

import sqlite3

# Retrieve data from database
def getData():
	conn=sqlite3.connect('data.db',check_same_thread=False)
	curs=conn.cursor()

	for row in curs.execute("SELECT * FROM block1 ORDER BY date DESC LIMIT 1"):
		date = str(row[1])
		id = row[0]
		o2_slev = row[2]
		o2_sprav = row[3]
		q_gaz = row[4]
		t_para_nitk_a = row[5]
		t_para_nitk_b = row[6]
		p_para = row[7]
		q_per_par = row[8]
		q_pit_voda = row[9]
		t_vozdh_posl_rvpa = row[10]
		t_vozdh_posl_rvpb = row[11]
		t_vozdh_posl_tvp_slev = row[12]
		t_vozdh_posl_tvp_sprav = row[13]
		t_posle_ekonomiz_slev = row[14]
		t_posle_ekonomiz_sprav = row[15]
		t_dym_zarvp_slev = row[16]
		t_dym_zarvp_sprav = row[17]
		t_dym_zatvp_slev = row[18]
		t_dym_zatvp_sprav = row[19]
		t_pitvod_kotl = row[20]
		t_uhodgaz_ventur1 = row[21]
		t_uhodgaz_ventur2 = row[22]
		t_mazut = row[23]
		t_uhodgaz_ventur3 = row[24]
		t_uhodgaz_ventur4 = row[25]
		t_kontensat_sbor = row[26]
		t_kontensat_vihkollect = row[27]
		t_vod_kollect_slev = row[28]
		t_vod_kollect_sprav = row[29]
		t_gaz_dsa = row[30]
		t_gaz_dsb = row[31]
		t_vozdh_pered_rvpa = row[32]
		t_vozdh_pered_rvpb = row[33]
		t_vozdh_pered_tvpslev = row[34]
		t_vozdh_pered_tvpsprav = row[35]
		h_baraban_slev = row[36]
		h_baraban_sprav = row[37]
		p_par_do_sk = row[38]
		q_par = row[39]
		t_par_posle_sk = row[40]
		vakum = row[41]
		t_par_psg1_prov1 = row[42]
		t_par_psg1_prov2 = row[43]
		t_par_psg2 = row[44]
		t_vod_do_psg1 = row[45]
		t_vod_posle_psg1 = row[46]
		t_vod_vihod_psg12 = row[47]
		t_par_posle_ou1 = row[48]
		t_par_posle_ou2 = row[49]
		t_kondesat_do_kn = row[50]
		t_cirk_vod_posle_kondensat = row[51]
		t_cirk_vod_do_kondensat = row[52]
		t_par_cnd_sprav = row[53]
		t_par_cnd_slev = row[54]
		t_par_uplotn_kollect = row[55]
		t_kondest_posle_pnd4 = row[56]
		t_vod_obvod_pvd7 = row[57]
		t_par_pered_pn130 = row[58]
		t_vod_posle_pvd7 = row[59]
		p_par_k_psg1 = row[60]
		p_par_k_psg2 = row[61]
		akt_stal_vozb_paz_7 = row[62]
		akt_stal_vozb_paz_21 = row[63]
		akt_stal_vozb_paz_36 = row[64]
		akt_stal_vozb_paz_50 = row[65]
		akt_stal_vozb_paz_64 = row[66]
		akt_stal_vozb_paz_77 = row[67]
		akt_stal_vozb_paz_3g7 = row[68]
		akt_stal_vozb_paz_25g10 = row[69]
		akt_stal_vozb_paz_44g12 = row[70]
		akt_stal_vozb_paz_3g13 = row[71]
		akt_stal_vozb_paz_25g16 = row[72]
		akt_stal_vozb_paz_44g18 = row[73]
		t_vod_sobstv_nuzht = row[74]
		t_vod_glav_korp_truba1 = row[75]
		t_vod_glav_korp_truba2 = row[76]
		t_vod_za_psn1 = row[77]
		t_vod_za_psn2 = row[78]
	conn.close()
	return date, id, o2_slev, o2_sprav, q_gaz,t_para_nitk_a, t_para_nitk_b, p_para, q_per_par, q_pit_voda, t_vozdh_posl_rvpa, t_vozdh_posl_rvpb, t_vozdh_posl_tvp_slev, t_vozdh_posl_tvp_sprav, t_posle_ekonomiz_slev, t_posle_ekonomiz_sprav, t_dym_zarvp_slev, t_dym_zarvp_sprav, t_dym_zatvp_slev, t_dym_zatvp_sprav, t_pitvod_kotl, t_uhodgaz_ventur1, t_uhodgaz_ventur2, t_mazut, t_uhodgaz_ventur3, t_uhodgaz_ventur4, t_kontensat_sbor, t_kontensat_vihkollect, t_vod_kollect_slev,t_vod_kollect_sprav, t_gaz_dsa, t_gaz_dsb, t_vozdh_pered_rvpa, t_vozdh_pered_rvpb, t_vozdh_pered_tvpslev, t_vozdh_pered_tvpsprav,h_baraban_slev, h_baraban_sprav, p_par_do_sk, q_par, t_par_posle_sk, vakum, t_par_psg1_prov1, t_par_psg1_prov2, t_par_psg2, t_vod_do_psg1, t_vod_posle_psg1, t_vod_vihod_psg12, t_par_posle_ou1, t_par_posle_ou2, t_kondesat_do_kn, t_cirk_vod_posle_kondensat, t_cirk_vod_do_kondensat, t_par_cnd_sprav, t_par_cnd_slev, t_par_uplotn_kollect, t_kondest_posle_pnd4, t_vod_obvod_pvd7, t_par_pered_pn130, t_vod_posle_pvd7, p_par_k_psg1, p_par_k_psg2, akt_stal_vozb_paz_7, akt_stal_vozb_paz_21, akt_stal_vozb_paz_36, akt_stal_vozb_paz_50, akt_stal_vozb_paz_64, akt_stal_vozb_paz_77, akt_stal_vozb_paz_3g7, akt_stal_vozb_paz_25g10, akt_stal_vozb_paz_44g12, akt_stal_vozb_paz_3g13, akt_stal_vozb_paz_25g16, akt_stal_vozb_paz_44g18, t_vod_sobstv_nuzht, t_vod_glav_korp_truba1, t_vod_glav_korp_truba2, t_vod_za_psn1, t_vod_za_psn2             

# main route 
@app.route("/")
def index():
	
	date, id, o2_slev, o2_sprav, q_gaz,t_para_nitk_a, t_para_nitk_b, p_para, q_per_par, q_pit_voda, t_vozdh_posl_rvpa, t_vozdh_posl_rvpb, t_vozdh_posl_tvp_slev, t_vozdh_posl_tvp_sprav, t_posle_ekonomiz_slev, t_posle_ekonomiz_sprav, t_dym_zarvp_slev, t_dym_zarvp_sprav, t_dym_zatvp_slev, t_dym_zatvp_sprav, t_pitvod_kotl, t_uhodgaz_ventur1, t_uhodgaz_ventur2, t_mazut, t_uhodgaz_ventur3, t_uhodgaz_ventur4, t_kontensat_sbor, t_kontensat_vihkollect, t_vod_kollect_slev,t_vod_kollect_sprav, t_gaz_dsa, t_gaz_dsb, t_vozdh_pered_rvpa, t_vozdh_pered_rvpb, t_vozdh_pered_tvpslev, t_vozdh_pered_tvpsprav,h_baraban_slev, h_baraban_sprav, p_par_do_sk, q_par, t_par_posle_sk, vakum, t_par_psg1_prov1, t_par_psg1_prov2, t_par_psg2, t_vod_do_psg1, t_vod_posle_psg1, t_vod_vihod_psg12, t_par_posle_ou1, t_par_posle_ou2, t_kondesat_do_kn, t_cirk_vod_posle_kondensat, t_cirk_vod_do_kondensat, t_par_cnd_sprav, t_par_cnd_slev, t_par_uplotn_kollect, t_kondest_posle_pnd4, t_vod_obvod_pvd7, t_par_pered_pn130, t_vod_posle_pvd7, p_par_k_psg1, p_par_k_psg2, akt_stal_vozb_paz_7, akt_stal_vozb_paz_21, akt_stal_vozb_paz_36, akt_stal_vozb_paz_50, akt_stal_vozb_paz_64, akt_stal_vozb_paz_77, akt_stal_vozb_paz_3g7, akt_stal_vozb_paz_25g10, akt_stal_vozb_paz_44g12, akt_stal_vozb_paz_3g13, akt_stal_vozb_paz_25g16, akt_stal_vozb_paz_44g18, t_vod_sobstv_nuzht, t_vod_glav_korp_truba1, t_vod_glav_korp_truba2, t_vod_za_psn1, t_vod_za_psn2 = getData()
	templateData = {
	  	'date'			: date,
      	'id'			: id,
      	'o2_slev'		: o2_slev,
	  	'o2_sprav'		:	o2_sprav,
		'q_gaz' 		:	q_gaz,
		't_para_nitk_a'	:	t_para_nitk_a,
		't_para_nitk_b' :	t_para_nitk_b,
		'p_para'		:	p_para,
		'q_per_par'		:	q_per_par,
		'q_pit_voda'	:	q_pit_voda,
		't_vozdh_posl_rvpa' :	t_vozdh_posl_rvpa,	
		't_vozdh_posl_rvpb' :	t_vozdh_posl_rvpb,
		't_vozdh_posl_tvp_slev' :	t_vozdh_posl_tvp_slev,
		't_vozdh_posl_tvp_sprav' :	t_vozdh_posl_tvp_sprav,
		't_posle_ekonomiz_slev' :	t_posle_ekonomiz_slev,
		't_posle_ekonomiz_sprav' :	t_posle_ekonomiz_sprav,
		't_dym_zarvp_slev' 		:	t_dym_zarvp_slev,
		't_dym_zarvp_sprav' 	:	t_dym_zarvp_sprav,
		't_dym_zatvp_slev' 		:	t_dym_zatvp_slev,
		't_dym_zatvp_sprav' 	:	t_dym_zatvp_sprav,
		't_pitvod_kotl' 		:	t_pitvod_kotl,
		't_uhodgaz_ventur1' 	:	t_uhodgaz_ventur1,
		't_uhodgaz_ventur2' 	:	t_uhodgaz_ventur2,
		't_mazut' 				:	t_mazut,
		't_uhodgaz_ventur3' 	:	t_uhodgaz_ventur3,
		't_uhodgaz_ventur4' 	:	t_uhodgaz_ventur4,
		't_kontensat_sbor' 		:	t_kontensat_sbor,
		't_kontensat_vihkollect' :	t_kontensat_vihkollect,
		't_vod_kollect_slev' 	:	t_vod_kollect_slev,
		't_vod_kollect_sprav' 	:	t_vod_kollect_sprav,
		't_gaz_dsa' 			:	t_gaz_dsa,
		't_gaz_dsb' 			:	t_gaz_dsb,
		't_vozdh_pered_rvpa' 	:	t_vozdh_pered_rvpa,
		't_vozdh_pered_rvpb' 	:	t_vozdh_pered_rvpb,
		't_vozdh_pered_tvpslev' :	t_vozdh_pered_tvpslev,
		't_vozdh_pered_tvpsprav' :	t_vozdh_pered_tvpsprav,
		'h_baraban_slev' 		:	h_baraban_slev,
		'h_baraban_sprav' 		:	h_baraban_sprav,
		'p_par_do_sk' 			:	p_par_do_sk,
		'q_par' 				:	q_par,
		't_par_posle_sk' 		:	t_par_posle_sk,
		'vakum' 				:	vakum,
		't_par_psg1_prov1' 		:	t_par_psg1_prov1,
		't_par_psg1_prov2' 		:	t_par_psg1_prov2,
		't_par_psg2'			:	t_par_psg2,
		't_vod_do_psg1' 		:	t_vod_do_psg1,
		't_vod_posle_psg1' 		:	t_vod_posle_psg1,
		't_vod_vihod_psg12' 	:	t_vod_vihod_psg12,
		't_par_posle_ou1' 		:	t_par_posle_ou1,
		't_par_posle_ou2' 		:	t_par_posle_ou2,
		't_kondesat_do_kn' 		:	t_kondesat_do_kn,
		't_cirk_vod_posle_kondensat '	:	t_cirk_vod_posle_kondensat,
		't_cirk_vod_do_kondensat' 	:	t_cirk_vod_do_kondensat,
		't_par_cnd_sprav' 		:	t_par_cnd_sprav,
		't_par_cnd_slev' 		:	t_par_cnd_slev,
		't_par_uplotn_kollect' 	:	t_par_uplotn_kollect,
		't_kondest_posle_pnd4' 	:	t_kondest_posle_pnd4,
		't_vod_obvod_pvd7' 		:	t_vod_obvod_pvd7,
		't_par_pered_pn130' 	:	t_par_pered_pn130,
		't_vod_posle_pvd7' 		:	t_vod_posle_pvd7,
		'p_par_k_psg1' 			:	p_par_k_psg1,
		'p_par_k_psg2' 			:	p_par_k_psg2,
		'akt_stal_vozb_paz_7' 	:	akt_stal_vozb_paz_7,
		'akt_stal_vozb_paz_21' 	:	akt_stal_vozb_paz_21,
		'akt_stal_vozb_paz_36' 	:	akt_stal_vozb_paz_36,
		'akt_stal_vozb_paz_50' 	:	akt_stal_vozb_paz_50,
		'akt_stal_vozb_paz_64' 	:	akt_stal_vozb_paz_64,
		'akt_stal_vozb_paz_77' 	:	akt_stal_vozb_paz_77,
		'akt_stal_vozb_paz_3g7' :	akt_stal_vozb_paz_3g7,
		'akt_stal_vozb_paz_25g10' :	akt_stal_vozb_paz_25g10,
		'akt_stal_vozb_paz_44g12' :	akt_stal_vozb_paz_44g12,
		'akt_stal_vozb_paz_3g13' :	akt_stal_vozb_paz_3g13,
		'akt_stal_vozb_paz_25g16' :	akt_stal_vozb_paz_25g16,
		'akt_stal_vozb_paz_44g18' :	akt_stal_vozb_paz_44g18,
		't_vod_sobstv_nuzht' 	:	t_vod_sobstv_nuzht,
		't_vod_glav_korp_truba1' :	t_vod_glav_korp_truba1,
		't_vod_glav_korp_truba2' :	t_vod_glav_korp_truba2,
		't_vod_za_psn1'  		:	t_vod_za_psn1,
		't_vod_za_psn2' 		:	t_vod_za_psn2
	}
	return render_template('index.html', **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5070, debug=False)

