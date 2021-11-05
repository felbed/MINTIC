public class Prestamo {
    private int IdUsuario;
    private String IdBicicleta;
    private String ModeloBicicleta;

    // Constructor
    // Parámetros constructor
    public Prestamo(int IdUsuario, String IdBicicleta, String ModeloBicicleta) {
        this.IdUsuario = IdUsuario;
        this.IdBicicleta = IdBicicleta;
        this.ModeloBicicleta = ModeloBicicleta;
    }

    public int getIdUsuario() {
        return IdUsuario;
    }

    public void setIdUsuario(int IdUsuario) {
        this.IdUsuario = IdUsuario;
    }

    public String getIdBicicleta() {
        return IdBicicleta;
    }

    public void setIdBicicleta(String IdBicicleta) {
        this.IdBicicleta = IdBicicleta;
    }

    public String getModeloBicicleta() {
        return ModeloBicicleta;
    }

    public void setModeloBicicleta(String ModeloBicicleta) {
        this.ModeloBicicleta = ModeloBicicleta;
    }

    public static int ConsultarDescuento(Prestamo[] historialPrestamos, Prestamo nuevoPrestamo){
        int descuento;
        int numeroPrestamos = 0;
        String modelo = nuevoPrestamo.getModeloBicicleta();
        for (int i = 0; i < historialPrestamos.length; i++) { 		      
            if (historialPrestamos[i].getIdUsuario() == nuevoPrestamo.getIdUsuario()) {
                numeroPrestamos++;
            } 	
        }

        if (numeroPrestamos < 3) {
            descuento = 0;
        } else if (numeroPrestamos >= 3 && numeroPrestamos <= 5) {
            descuento = 4;
        } else {
            descuento = 6;
            switch (modelo){
                case "Standard":
                    descuento += 2;
                    break;
                case "Premium":
                    descuento += 3;
                    break;
            }
        }

        return descuento;
    }
}
