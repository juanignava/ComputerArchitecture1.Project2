module memoryAccess (input logic clk, memWriteM, switchStart,
							  input logic [31:0] A, wd,
							  output logic [31:0] rd);

	

	memoryController memoryControllerUnit (clk, memWriteM, switchStart, 
														A, wd,
														rd);

endmodule 