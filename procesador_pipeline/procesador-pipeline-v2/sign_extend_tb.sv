module sign_extend_tb ();
	
	logic clk;
	logic [26:0] num_in;
	logic [1:0] imm_src;
	logic [31:0] num_out;
	
	sign_extend sign_extend_TB (num_in, imm_src, num_out);
	
	initial begin
		
		clk = 0; #2;
		
		// Extend test 1:
		num_in = 27'b000111100111111000011110000; imm_src = 2'b00; #2
		
		// Extend test 2:
		num_in = 27'b000111100111111000011110000; imm_src = 2'b01; #2
		
		// Extend test 3:
		num_in = 27'b000111100111111000011110000; imm_src = 2'b10; #2
		
		// Extend test 4:
		num_in = 27'b000111100111111000011110000; imm_src = 2'b11; #2;
		
	end
	
	always begin
		clk=!clk; #1;
	end
	
endmodule 