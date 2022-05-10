module testbench ();

	// Test bench del modulo register_file
	
	logic [3:0] RS1, RS2, RS3, RD;
	logic [31:0] WD, RD1, RD2, RD3;
	logic wr_enable, clk, rst;
	
	register_file register_file(RS1, RS2, RS3, RD, WD, wr_enable, clk, rst, 
										RD1, RD2, RD3);
	
	
	always begin
	
		#10 clk = ~ clk; // Un ciclo de reloj equivale a 10 unidades de tiempo
	
	end
	
	initial begin
	
		clk = 0;
		rst = 1;
		RS1 = 4'd0;
		RS2 = 4'd0;
		RS3 = 4'd0;
		WD = 31'd0;
		wr_enable = 0;
		
		#20
		
		// escribir en el registro 3 un 99
		
		rst = 0;
		wr_enable = 1;
		RD = 4'd3;
		WD = 31'd99;
		
		#20
		
		// escribir en el resgitro 4 un 50 con wr_enable en 0 (no debe escribir)
		
		wr_enable = 0;
		RD = 4'd4;
		WD = 31'd50;
		
		#20
		
		// escribir en el resgitro 5 un 255
		
		wr_enable = 1;
		RD = 4'd5;
		WD = 31'd255;
		
		#20
		
		// leer del registro 3 y 5 el valor que tienen
		
		wr_enable = 0;
		RS1 = 4'd3;
		RS2 = 4'd5;	
	
		#20
		rst = 0;
		wr_enable = 1;
		RD = 4'd3;
		WD = 31'd2;
		
		
		
	
	end

endmodule 