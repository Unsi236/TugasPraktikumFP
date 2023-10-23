//Dalam Bahasa Dart

//KODE1
List<int> sequenceGenerator(int start, int stop) => [for (var i = start; i <= stop; i++) i];
List<int> Kode1 = sequenceGenerator(0,9);

//KODE2
List<String> fizzBuzz(int a, int b) => [for (int i = a; i < b; i++) (i % 3 == 0 && i % 5 == 0) ? "FizzBuzz" : (i % 3 == 0) ? "Fizz" : (i % 5 == 0) ? "Buzz" : i.toString()];
List<String> Kode2 = fizzBuzz(0, 9);

//KODE3
List<int> twoNumber(List<int> l) => [for (var i = 0; i < l.length - 1; i++) l[i] + l[i + 1]];
List<int> Kode3 = twoNumber([6,7,8,9,10,11,12,13]);


void main(){
    print(Kode1);
    print(Kode2);
    print(Kode3);
}