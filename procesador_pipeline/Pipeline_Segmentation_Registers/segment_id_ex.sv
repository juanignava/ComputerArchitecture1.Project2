 module segment_id_ex (input logic clk, rst,
								input logic MemToReg_in, MemRead_in, MemWrite_in, 
								input logic [2:0] ALUOp_in, 
								input logic ALUSrc_in, RegWrite_in,
								input logic [31:0] pc_in, RD1_in, RD2_in, RD3_in, 
								input logic [3:0] RR3_in,
								input logic [31:0] num_in,
								output logic MemToReg_out, MemRead_out, MemWrite_out, 
								output logic [2:0] ALUOp_out, 
								output logic ALUSrc_out, RegWrite_out,
								output logic [31:0] pc_out, RD1_out, RD2_out, RD3_out, 
								output logic [3:0] RR3_out,
								output logic [31:0] num_out);
			
	always_ff@(negedge clk, posedge rst)
		if(rst)
			begin
				MemToReg_out = 0;
				MemRead_out = 0;
				MemWrite_out = 0;
				ALUOp_out = 0;
				ALUSrc_out = 0;
				RegWrite_out = 0;
				pc_out = 0;
				RD1_out = 0;
				RD2_out = 0;
				RD3_out = 0;
				RR3_out = 0;
				num_out = 0;
			end
			
		else 
			begin
				MemToReg_out = MemToReg_in;
				MemRead_out = MemRead_in;
				MemWrite_out = MemWrite_in;
				ALUOp_out = ALUOp_in;
				ALUSrc_out = ALUSrc_in;
				RegWrite_out = RegWrite_in;
				pc_out = pc_in;
				RD1_out = RD1_in;
				RD2_out = RD2_in;
				RD3_out = RD3_in;
				RR3_out = RR3_in;
				num_out = num_in;
			end
		
endmodule