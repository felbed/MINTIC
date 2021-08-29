import java.util.Arrays;

public class Inicio {
    public static void main(String[] args) {

        String[] Estaciones = {"Parque de las luces", "Belén", "Guayabal"};
        boolean orden = false;

        System.out.println(Arrays.toString(Estaciones));

        Arrays.sort(Estaciones);

        if (orden == false) {
            int i = 0;
            int j = Estaciones.length-1;
            String temp;

            while(i<j){
                //intercambia
                temp = Estaciones[i];
                Estaciones[i] = Estaciones[j];
                Estaciones[j] = temp;
            
                //actualiza i y j
                i++;  
                j--;
            }    
        }

        System.out.println(Arrays.toString(Estaciones));
    }
}