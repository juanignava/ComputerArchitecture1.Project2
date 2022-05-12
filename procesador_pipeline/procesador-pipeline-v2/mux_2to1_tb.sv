module mux_2to1_tb ();
	
	logic clk;
	logic [31:0] A, B;
	logic sel;
	logic [31:0] C;
	
	mux_2to1 mux_2to1_TB (A, B, sel, C);
	
	initial begin
		
		clk = 0; #2;
		
		// Mux 2 to 1, test 1:
		A = 32'b11110000111100001111000011110000; B = 32'b10000000000000000000000000000001; sel = 1'b0; #2
		
		// Mux 2 to 1, test 2:
		A = 32'b11110000111100001111000011110000; B = 32'b10000000000000000000000000000001; sel = 1'b1; #2;
		
	end
	
	always begin
		clk=!clk; #1;
	end
	
endmodule