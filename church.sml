datatype 'a inf_list = lcons of 'a * (unit -> 'a inf_list)

fun church(s)=let fun thk()=church("(f "^s^")")
		in lcons("Lf.Lx.(f "^s^")",thk)
		end;

fun take(0, _) = []
 | take(n, lcons(h, thk)) = h :: take(n-1, thk());
take(5,church("x"))
