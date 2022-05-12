module control_unit_tb ();

	logic clk;
	logic [1:0] instruction_type; 
	logic [4:0] func;
	logic rst;
	logic JumpI, JumpCI, JumpCD, MemToReg, MemRead, MemWrite; 
	logic [2:0] ALUOp;
	logic ALUSrc, RegWrite;
	logic [1:0] ImmSrc, RegDtn; 
	logic RegSrc2; 
	logic [1:0] RegSrc1;
	
	control_unit control_unit_TB (instruction_type, 
											func, 
											rst, 
											JumpI, JumpCI, JumpCD, MemToReg, MemRead, MemWrite, 
											ALUOp,
											ALUSrc, RegWrite,
											ImmSrc, RegDtn,
											RegSrc2,
											RegSrc1);
	
	initial begin
		
		clk = 0; #2;
		
		rst = 1; #2
		rst = 0; #2
		
		//---- Instrucciones de Datos sin inmediato----//
		
		// Control Unit, SUM test:
		instruction_type = 2'b10;
		func = 5'b00000; #2
		
		// Control Unit, RES test:
		instruction_type = 2'b10;
		func = 5'b00001; #2
		
		// Control Unit, MUL test:
		instruction_type = 2'b10;
		func = 5'b00010; #2
		
		// Control Unit, DIV test:
		instruction_type = 2'b10;
		func = 5'b00011; #2
		
		// Control Unit, RSD test:
		instruction_type = 2'b10;
		func = 5'b00100; #2
		
		//---- Instrucciones de Datos con inmediato----//
		
		// Control Unit, SUMI test:
		instruction_type = 2'b10;
		func = 5'b11000; #2
		
		// Control Unit, RESI test:
		instruction_type = 2'b10;
		func = 5'b11001; #2
		
		// Control Unit, MULI test:
		instruction_type = 2'b10;
		func = 5'b11010; #2
		
		// Control Unit, DIVI test:
		instruction_type = 2'b10;
		func = 5'b11011; #2
		
		// Control Unit, RSDI test:
		instruction_type = 2'b10;
		func = 5'b11100; #2
		
		//---- Instrucciones de Control----//
		
		// Control Unit, SI test:
		instruction_type = 2'b00;
		func = 5'b00000; #2
		
		// Control Unit, SCI test:
		instruction_type = 2'b00;
		func = 5'b00010; #2
		
		// Control Unit, SCD test:
		instruction_type = 2'b00;
		func = 5'b00011; #2
		
		//---- Instrucciones de Memoria----//
		
		// Control Unit, GDR test:
		instruction_type = 2'b01;
		func = 5'b00000; #2
		
		// Control Unit, CRG test:
		instruction_type = 2'b01;
		func = 5'b00001; #2;
		
	end
	
	always begin
		clk=!clk; #1;
	end
	
endmodule