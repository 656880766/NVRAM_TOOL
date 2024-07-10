#ifndef _CONF_H
#define _CONF_H
#include "nvmaems_msg.h" 
#include "aemsrnm_nvm_writeonfly.h" 



/* START definitions for Block 'Block2' */ 

 typedef struct {
 	/* CRC value for current block */ 
   uint8_t Crc8_u8;
 	/* variables definition */ 
    boolean var3;
    boolean var4;
}Block2_t  ; 

 extern  Block2_t  Block2_CST_RamBlk; 

 #endif // CONF_H
