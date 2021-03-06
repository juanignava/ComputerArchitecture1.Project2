module dmem_rom (input logic [31:0] address,
				output logic [31:0] rd);
	
	logic [31:0] dmem_ROM[0:8099];
	
	initial
	
		// Data meant to be read
		// DIRECCIÓN DE JOSE
		$readmemh("C:/altera/14.1/procesador_pipeline/imageData.txt", dmem_ROM);
		// DIRECCIÓN DE NACHO NAVARRO
		//$readmemh("C:/arqui-1/procesador-pipeline/imageData.txt", dmem_ROM);
		
		
	assign rd = dmem_ROM[address[31:0]];
	
endmodule 