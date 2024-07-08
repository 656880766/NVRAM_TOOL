#ifndef _TEMPLATE_CONF_H
#define _TEMPLATE_CONF_H

#include "nvmaems_msg.h"
#include "aemsrnm_nvm_writeonfly.h"

/* START definitions for Block 'A_CHANNEL_1' */

typedef struct {
/* CRC value for current block */
uint8 Crc8_u8;
/* variables definition */
uint8 Vnt_lim_perf_hist_100ms_NV[10];
uint8 Vnx_ac_cmbo_chg_plg_lck_typ_did_stt_conf_NV;
uint8 Vnx_ac_cmbo_chg_plg_lck_typ_stt_conf_NV;
uint8 Vnx_ac_v2l_avl_did_stt_conf_NV;
uint8 Vnx_ac_v2l_out_plg_typ1_jpn_frq_sp_NV;
uint8 Vnx_hvsys_fail_pchg_cnt_NV;
} A_CHANNEL_1_t;

extern A_CHANNEL_1_t A_CHANNEL_1_CST_RamBlk;


