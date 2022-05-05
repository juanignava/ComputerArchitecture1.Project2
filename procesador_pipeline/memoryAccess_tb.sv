module memoryAccess_tb ();

	logic clk, memWriteM, switchStart;
	logic [31:0] A, wd;
	logic [31:0] rd;

	memoryAccess memory (clk, memWriteM, switchStart, A, wd, rd);
	
	initial begin
		
		clk = 0; switchStart = 0; #1;
		
		switchStart = 1; #1;
		
		// Writing on RAM test 1:
		A = 33136; #1
		
		memWriteM = 1; wd = 33; #1
		
		// Writing on RAM test 2:
		A = 33135; #1
		
		memWriteM = 1; wd = 45; #1
		
		// Reading from ROM test 1:
		
		A = 735; #1
		
		memWriteM = 0; #1
		
		// Writing on RAM test 3:
		A = 33137; #1
		
		memWriteM = 1; wd = 222; #1
		
		switchStart = 1; #1;
		
		// We need to test Reading from RAM! Some issues may appear.

	end
	
	always begin
		clk=!clk; #1;
	end
	
endmodule 