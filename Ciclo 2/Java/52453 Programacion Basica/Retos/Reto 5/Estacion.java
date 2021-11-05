import java.util.Arrays;
import java.util.HashMap;

public class Estacion {
    private String Ubicacion;
    private Bicicleta[] Bicicletas;
    private int CantidadPrestamos;

    public Estacion(String Ubicacion, Bicicleta[] Bicicletas, int CantidadPrestamos) {
        this.Ubicacion = Ubicacion;
        this.Bicicletas = Bicicletas;
        this.CantidadPrestamos = CantidadPrestamos;
    }

    public String getUbicacion() {
        return Ubicacion;
    }

    public Bicicleta[] getBicicletas() {
        return Bicicletas;
    }

    public int getCantidadPrestamos() {
        return CantidadPrestamos;
    }

    public static Estacion[] ConsultarEstacionesMasUsadas(Estacion[] Estaciones) {
        Estacion[] masUsadas = new Estacion[3];
        int n = Estaciones.length;
        for (int i = 0; i < (n - 1); i++) {
            for (int j = 0; j < (n - i - 1); j++) {
                if(Estaciones[j].getCantidadPrestamos() < Estaciones[j + 1].getCantidadPrestamos()) {
                    Estacion temporal = Estaciones[j];
                    Estaciones[j] = Estaciones[j + 1];
                    Estaciones[j + 1] = temporal;
                }
            }
        }

        for (int i = 0; i < masUsadas.length; i++) {
            masUsadas[i] = Estaciones[i];
        }

        return masUsadas;
    }

    public HashMap<String, Integer> getBalanceBicicletas() {
        HashMap<String, Integer> Balance = new HashMap<String, Integer>();
        Bicicleta[] Bicicletas = this.getBicicletas();
        for (int i = 0; i < Bicicletas.length; i++) {
            String Modelo = Bicicletas[i].getModelo();
            if (!Balance.containsKey(Modelo)) {
                Balance.put(Modelo, 1);
            } else {
                Balance.replace(Modelo, Balance.get(Modelo), Balance.get(Modelo) + 1);
            }
        }
        return Balance;
    }

    public int ConsultarProgreso() {
        HashMap<String, Integer> Balance = this.getBalanceBicicletas();
        int totalBicicletas = this.getBicicletas().length;
        int premium = Balance.get("Premium");
        int porcentaje = 0;

        porcentaje = Math.round((premium * 100) /totalBicicletas);

        return porcentaje;
    }

    public static String ConsultarUbicaciones(Estacion[] Estaciones, boolean orden) {
        if (orden == true) {
            Arrays.sort(Estaciones);
        } else {
            Arrays.sort(Estaciones, Estaciones.length, 0);
        }
        return Arrays.toString(Estaciones);
    }
}
