module memorySegmentation (input logic clk, rst, we, switchStart,
					 input logic [31:0] address, wd,
					 output logic [31:0] rd,
					 output logic GPIO,GPIOFlag
);
						 
	logic [31:0] mapAddress, romData, ramData;
						 
	dmem_ram ram(clk, we, mapAddress, wd, ramData);
	imem rom(mapAddress, romData);
	
	always_comb
		begin
		
			// Instructions.
			if (address >= 'd0 && address < 'd735)
				begin
					mapAddress = address;
					rd = romData;
					GPIO = 1'b0;
					GPIOFlag = 1'b0;
				end
			
			// Reading data (loads).
			else if (address >= 'd735 && address < 'd33135)
				begin
					mapAddress = address;
					rd = ramData;
					GPIO = 1'b0;
					GPIOFlag = 1'b0;
				end
				
			// Reading starting switch value saved in this address.
			else if (address == 'd33135)
				begin
					mapAddress = 32'b0;
					rd = {31'b0, switchStart};
					GPIO = 1'b0;
					GPIOFlag = 1'b0;
				end
				
			// "we" value as 1 means we have to rise the GPIOFlag to write in the output.txt (testbench logic).
			else if (address == 'd33135 && we == 1'b1)
				begin
					GPIO = wd[0];
					GPIOFlag = 1'b1;
					mapAddress = 32'b0;
					rd = 32'b0;
				end
			// if nothing happens, rst case.
			else
				begin
					GPIO = 1'b0;
					GPIOFlag = 1'b0;
					mapAddress = 32'b0;
					rd = 32'b0;
				end
		end
						 
endmodule 