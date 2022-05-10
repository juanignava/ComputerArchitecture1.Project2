module jump_unit_testbench();
	
	logic FlagZ;
	logic JumpCD;
	logic JumpCI;
	logic JumpI;
	logic PCSource;
			
	jump_unit jump(FlagZ, JumpCD, JumpCI, JumpI, PCSource);
	
	initial begin
	
	
		// Memoria, datos con immediato y datos sin immediato
		FlagZ = 0;
		JumpCD = 0;
		JumpCI = 0;
		JumpI = 0;
	
		#40
		
		FlagZ = 1;
		JumpCD = 0;
		JumpCI = 0;
		JumpI = 0;
	
		#40
		
		// Control SI
		FlagZ = 0;
		JumpCD = 0;
		JumpCI = 0;
		JumpI = 1;
	
		#40
		
		FlagZ = 1;
		JumpCD = 0;
		JumpCI = 0;
		JumpI = 1;
			
		#40
		
		// Control SCI
		FlagZ = 0;
		JumpCD = 0;
		JumpCI = 1;
		JumpI = 0;
	
		#40
		
		FlagZ = 1;
		JumpCD = 0;
		JumpCI = 1;
		JumpI = 0;
	
		#40
		
		// Control SCD
		FlagZ = 0;
		JumpCD = 1;
		JumpCI = 0;
		JumpI = 0;
	
		#40
		
		FlagZ = 1;
		JumpCD = 1;
		JumpCI = 0;
		JumpI = 0;
				
	end

endmodule
