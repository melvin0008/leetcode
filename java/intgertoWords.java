public class Solution {
    public String[] oneToNineteen = new String[]{
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen"
    };

    public String[] twentyToNinety = new String[]{
        "",
        "Ten",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety"
    };

    public String[] hunderedToBillion = new String[]{
        "Hundred",
        "Thousand",
        "Million",
        "Billion"
    };
    public String numberToWords(int num) {
      if(num==0){
          return "Zero";
      }  
      
      StringBuilder builder= new StringBuilder();
      convert(num,builder);
      return builder.toString().trim();
      
    }
    public void convert(int num,StringBuilder builder){
        if(num==0){
          return ;
        }
        if(num>0 && num<20){
            builder.append(oneToNineteen[num]);
            builder.append(" ");
        }
        else if(num<100){
            builder.append(twentyToNinety[num/10]);
            builder.append(" ");
            convert(num%10,builder);
        }
        else if(num<1000){
            convert(num/100,builder);
            builder.append(hunderedToBillion[0]);
            builder.append(" ");
            convert(num%100,builder);
        }
        else if(num<1000000){
            convert(num/1000,builder);
            builder.append(hunderedToBillion[1]);
            builder.append(" ");
            convert(num%1000,builder);
        }
        else if(num<1000000000){
            convert(num/1000000,builder);
            builder.append(hunderedToBillion[2]);
            builder.append(" ");
            convert(num%1000000,builder);
        }
        else{
            convert(num/1000000000,builder);
            builder.append(hunderedToBillion[3]);
            builder.append(" ");
            convert(num%1000000000,builder);
        }
        
    }
}