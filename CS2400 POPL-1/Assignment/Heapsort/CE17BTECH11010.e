note
	description: "HeapSort application root class"
	date: "$Date$"
	revision: "$Revision$"

class
	CE17BTECH11010

inherit
	ARGUMENTS_32

create
	make

--feature
--	swap_num( a : INTEGER; b : INTEGER)
--	local
--		c : INTEGER
--	do
--		c := b
--		b := a
--		a := c

--	end

feature
	heapify(arr : ARRAY[INTEGER] ; n : INTEGER ; i: INTEGER)
	local
		large : INTEGER
		left,right : INTEGER
		c : INTEGER

		do
			large := i
			left := 2*i + 1
			right := 2*i + 2
			if
				(left < n and arr[left] > arr[large])
			then
				large := left

			end

			if
				(right < n and arr[right] > arr[large])
			then
				large := right
			end

			if
				large /= i
			then
				c := arr[i]
				arr[i] := arr[large]
				arr[large] := c
				heapify(arr , n , large)
			end

		end


--feature
--	insert(arr : ARRAY[INTEGER] ; n : INTEGER ; value : INTEGER)
--	do
--		n := n + 1
--		arr[n-1] := value
--		heapify(arr, n , n - 1)
--	end


feature
	heapsort(arr : ARRAY[INTEGER] ; n : INTEGER)

		local
			j : INTEGER
			c : INTEGER
		do
			from
				j := (n//2) - 1
			until
				j >= 1
			loop
				heapify(arr,n,j)
				j := j - 1
			end


			from
				j := n - 1
			until
				j >= 1
			loop
				c := arr[j]
				arr[j] := arr[1]
				arr[1] := c
				heapify(arr , j , 1)
				j := j - 1
			end
		end

feature

	make
		local
			Array : ARRAY[INTEGER]
			i,t : INTEGER
			input_file : PLAIN_TEXT_FILE
			output_file : PLAIN_TEXT_FILE
			in_path : STRING
			out_path : STRING
			size : INTEGER

		do
			in_path := "input.txt"
	  		out_path := "output.txt"
	  	create input_file.make(in_path)
	  		input_file.open_read
	  		input_file.read_integer
	  		size := input_file.last_integer  --size of array
	  		create Array.make_filled(0,1,size)

	  			--taking input from text file and filling  array
	  		from
	  			i := 1
	  		until
	  			i > size
	  		loop
	  			input_file.read_integer
	  			Array[i] := input_file.last_integer
	  			--io.put_integer (Array[i])
	  			--io.put_new_line
	  			i := i + 1
	  		end
	  		input_file.close

	  		heapsort(Array , size)
	  		create output_file.make_open_write (out_path)


	  		from
	  			i := 1
	  		until
	  			i > size
	  		loop
	  			--output_file.put_integer (Array[i])
	  			t := i - 1
	  			output_file.put_integer (t)

	  			output_file.put_string (" ")
	  			i := i + 1
	  		end
	  		output_file.close


		end -- do end

end --program end

