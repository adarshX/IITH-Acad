note
	description: "CE17BTECH11010 application root class"
	date: "$Date$"
	revision: "$Revision$"

class
	CE17BTECH11010

inherit
	ARGUMENTS_32

create
	make

-- function to find gcd for two numbers
feature
	gcd_num(num1 : INTEGER ; num2 : INTEGER ) : INTEGER

	local
		t1 : INTEGER
		t2 : INTEGER
		i : INTEGER

	do
		t1 := num1
		t2 := num2


		from
			i := 1
		until
			(i <= t1 and i <= t2)
		loop
			if
				(t1 \\ i = 0 and t2 \\ i = 0)
			then
				Result := i
			end
			i :=  i + 1
		end



	end

-- function to find inverse modulo
feature
	modular_inverse ( num : INTEGER ; div : INTEGER) : INTEGER
	local
		j : INTEGER
		t : INTEGER
	do
		from
			j :=1
		until
			j > div
		loop

			t := num * j

			if
				t \\ div = 1
			then
				Result := j
			end
			j := j +1

		end
	end





feature

	make
	  local
	  	num : ARRAY[INTEGER]
	  	rem : ARRAY[INTEGER]
	  	multiply : INTEGER
	  	i,j : INTEGER
	  	size : INTEGER
	  	x_min : INTEGER
	    temp1 , temp2 : INTEGER
	  	condition : BOOLEAN
	  	p_m : ARRAY[INTEGER]
	  	inv_mod : INTEGER
	  	t : INTEGER
	  	gcd_val : INTEGER
	  	input_file : PLAIN_TEXT_FILE
	  	output_file : PLAIN_TEXT_FILE
	  	in_path : STRING
	  	out_path : STRING



	  	do
	  		in_path := "input.txt"
	  		out_path := "output.txt"
	  	create input_file.make(in_path)
	  		input_file.open_read
	  		input_file.read_integer
	  		size := input_file.last_integer  --size of array
	  		io.put_integer (size)
	  		io.put_new_line
	  		--io.put_string ("enter no.of inputs")
	  		--io.read_integer    --change this line to input from text file


	  		x_min := 0
	  		multiply := 1
	  		condition := TRUE

	  		-- creating arrays
	  		create num.make_filled(0,1,size)
	  		create rem.make_filled (0,1, size)
	  		create p_m.make_filled (0,1, size)


	  		--taking input from text file and filling num and remainder arrays
	  		from
	  			i := 1
	  		until
	  			i > size
	  		loop
	  			input_file.read_integer
	  			temp1 := input_file.last_integer
	  			num[i] := temp1			-- fill num array
	  			--io.put_integer(num[i])
	  			--io.put_new_line
	  			input_file.read_integer
	  			temp2 := input_file.last_integer
	  			rem[i] := temp2
	  			io.put_integer(rem[i])
	  			io.put_new_line

	  			i := i + 1
	  		end


	  		input_file.close

	  		create output_file.make_open_write (out_path)

	  		--invalid input condition ( remainder greater than number)
	  		from
	  			i := 1
	  		until
	  			(i > size or condition =  FALSE)
	  		loop
	  			if
	  				rem[i] >= num[i]

	  			then
	  				--output_file.put_string ("INVALID")
	  				condition := FALSE

	  			end
	  			i := i + 1

	  		end


	--invalid input condition
	  		from
	  			i := 1
	  		until
	  			(i > size or condition =  FALSE)
	  		loop
	  			from
	  				j := i + 1
	  			until
	  				(j > size or condition = FALSE)
	  			loop
	  				gcd_val := gcd_num(num[i] , num[j])

	  				if
	  					gcd_val /= 1
	  				then
	  				--output_file.put_string ("INVALID")
	  				condition := FALSE
	  				end
	  				j := j + 1
	  			end
	  			i := i + 1
	  		end
	  		condition := TRUE
	  		io.put_boolean (condition)


	  		if
	  			condition = TRUE
	  		then
	  			from
	  				i := 1
	  			until
	  				i > size
	  			loop
	  				multiply := multiply * num[i]
	  				i := i + 1
	  			end

	  			from
	  				i := 1
	  			until
	  				i > size
	  			loop
	  				p_m[i] := multiply // num[i]
	  				i := i + 1
	  			end

	  			from
	  				i := 1
	  			until
	  				i > size
	  			loop
	  				inv_mod := modular_inverse(p_m[i] , num[i])
	  				t := rem[i] * p_m[i] * inv_mod
	  				x_min := x_min + t
	  				i := i + 1

	  			end

	  			x_min := x_min \\ multiply
	  			output_file.put_integer(x_min)
	  			output_file.new_line
	  			--io.put_integer(x_min)

	  		end -- if end
	  		output_file.close





	  	end  -- do end




end  --program end

