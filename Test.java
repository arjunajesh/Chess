import java.util.Calendar;

class Test{
    public static void main(String[] args){
        Calendar c = Calendar.getInstance();
        c.setLenient(false);
        c.set(2001, 1, 29);
        System.out.println(c.get(Calendar.DATE));
    }
}