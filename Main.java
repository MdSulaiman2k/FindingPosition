import java.util.* ;



class Main {
  
  static void print(boolean chka , int colison_of_a ){
    if(!chka )
      System.out.println("Yoda");
    else
      System.out.println(colison_of_a);
  }
  static Scanner kbd = new Scanner(System.in) ;
  public static void main(String[] args) {
    int a = kbd.nextInt() ;
    int b = kbd.nextInt() ;
    int colison_of_a  = 0 ;
    int colison_of_b  = 0 ;
    boolean chka = false ;
    boolean chkb = false  ;
    int x = 1 ; 
    int y = 1 ;
    while(a != 0 || b != 0){
      if(a%10 >  b%10){
        colison_of_a = (a%10)*x + colison_of_a ; 
        x = x*10 ;
        chka = true ;
      } 
      else if(a%10 < b%10){
         colison_of_b = (b%10)*y + colison_of_b ; 
          y = y*10 ;
          chkb = true ;
      }
      else{
        chkb = true ;
        chka = true ;
        colison_of_a = (a%10)*x + colison_of_a ; 
        x = x*10 ;
        colison_of_b = (b%10)*y + colison_of_b ; 
          y = y*10 ;
      }
      a = a/10 ;
      b = b/10 ;
      
    }


    print(chka ,colison_of_a  );
    print(chkb ,colison_of_b ) ;
    
    


    
    
    
  }
}