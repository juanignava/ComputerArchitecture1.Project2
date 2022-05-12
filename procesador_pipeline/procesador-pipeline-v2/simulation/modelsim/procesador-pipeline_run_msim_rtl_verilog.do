transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/adder.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/sign_extend.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/memoryAccess.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/memoryController.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/dmem_ram.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/mux_2to1.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/mux_4to1.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/pc_register.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/segment_ex_mem.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/segment_id_ex.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/segment_if_id.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/segment_mem_wb.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/alu.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/control_unit.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/procesador_pipeline.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/register_file.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/testbench.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/dmem_rom.sv}
vlog -sv -work work +incdir+C:/arqui-1/procesador-pipeline {C:/arqui-1/procesador-pipeline/imem.sv}

