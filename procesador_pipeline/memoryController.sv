module memoryController (input logic clk, we, switchStart,
					 input logic [31:0] address, wd,
					 output logic [31:0] rd
);
						 
	logic [31:0] mapAddress, romData, ramData;
						 
	dmem_ram ram (clk, we, mapAddress, wd, ramData);
	dmem_rom rom (mapAddress, romData);
	
	always_comb
		begin
		
			// Reading data from Rom.
			if (address >= 'd735 && address < 'd33135)
				begin
					mapAddress = address - 'd735;
					rd = romData;
				end
			
			// Reading from Ram.
			else if (address >= 'd33135 && address < 'd65536)
				begin
					mapAddress = address - 'd33135;
					rd = ramData;
				end
				
			// Case if nothing happens.
			else
				begin
					mapAddress = 32'b0;
					rd = 32'b0;
				end
		end
						 
endmodule 