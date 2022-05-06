transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vlog -sv -work work +incdir+C:/altera/14.1/procesador_pipeline {C:/altera/14.1/procesador_pipeline/dmem_ram.sv}
vlog -sv -work work +incdir+C:/altera/14.1/procesador_pipeline {C:/altera/14.1/procesador_pipeline/memoryController.sv}
vlog -sv -work work +incdir+C:/altera/14.1/procesador_pipeline {C:/altera/14.1/procesador_pipeline/memoryAccess.sv}
vlog -sv -work work +incdir+C:/altera/14.1/procesador_pipeline {C:/altera/14.1/procesador_pipeline/memoryAccess_tb.sv}
vlog -sv -work work +incdir+C:/altera/14.1/procesador_pipeline {C:/altera/14.1/procesador_pipeline/imem.sv}
vlog -sv -work work +incdir+C:/altera/14.1/procesador_pipeline {C:/altera/14.1/procesador_pipeline/dmem_rom.sv}

