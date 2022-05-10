module adder_tb ();
	
	logic clk;
	logic [31:0] A, B;
	logic [31:0] C;
	
	adder adder_TB (A, B, C);
	
	initial begin
		
		clk = 0; #2;
		
		// Adder, test 1:
		A = 32'b10000000000000000000000000000000; 
		B = 32'b10000000000000000000000000000001; #2
		
		// Adder, test 2:
		A = 32'b10000000000000000000000000000010; 
		B = 32'b10000000000000000000000000000001; #2
		
		// Adder, test 3:
		A = 32'b11111111111111111111111111111111; 
		B = 32'b00000000000000000000000000000001; #2;
		
	end
	
	always begin
		clk=!clk; #1;
	end
	
endmodule