module pc_register_testbench();
	
	logic clk;
	logic clr;
	logic load;
	logic [31:0] pc_in;
	logic [31:0] pc_out;
			
	pc_register pc(clk, clr, load, pc_in, pc_out);
									  
	always begin
	
		#10 clk = ~ clk;
	
	end
	
	initial begin	
		
		clk = 1;
		clr = 0;		
		load = 0;
		pc_in = 32'b00000000000000000000000000001111;
		
		#40
		
		clr = 1;
		load = 1;
		pc_in = 32'b00000000000000000000000000000111;
		
		#40
		
		load = 0;
		pc_in = 32'b00000000000000000000000000000011;
			
	end

endmodule
