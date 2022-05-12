module testbench();

	logic clk;
	logic rst;
	
	procesador_pipeline procesador(clk, rst);
	
	always begin
	
		#1 clk = ~clk; // medio ciclo de reloj equivale a una unidad
		
	end
	
	initial begin
		
		// señales iniciales
		rst = 1;
		clk = 1;
		
		#1
		
		rst = 0;
		
		#1;
		
	end
		
endmodule
