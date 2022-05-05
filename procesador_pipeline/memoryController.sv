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
			if (address >= 'd400 && address < 'd8500)
				begin
					mapAddress = address - 'd400;
					rd = romData;
				end
			
			// Reading or writing from Ram.
			else if (address >= 'd8500 && address < 'd138100)
				begin
					mapAddress = address - 'd8500;
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