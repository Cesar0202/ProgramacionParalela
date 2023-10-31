/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package procesamientoimagenesavanzado;

import com.googlecode.javacv.CanvasFrame;
import com.googlecode.javacv.FrameGrabber;
import com.googlecode.javacv.OpenCVFrameGrabber;
import com.googlecode.javacv.cpp.opencv_core;
import static com.googlecode.javacv.cpp.opencv_highgui.cvLoadImage;
import com.googlecode.javacv.cpp.opencv_imgproc;
import static com.googlecode.javacv.cpp.opencv_imgproc.cvCanny;

public class ProcesamientoImagenesAvanzado {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws FrameGrabber.Exception {
        // Cargamos la imagen
        opencv_core.IplImage imagenOriginal = cvLoadImage("D:\\imgPrueba2.jpg");

        // Verificamos si la imagen se cargó correctamente
        if (imagenOriginal == null) {
            System.out.println("No se pudo cargar la imagen.");
            return;
        }

        // Convertimos la imagen a escala de grises
        opencv_core.IplImage imagenGris = opencv_core.IplImage.create(imagenOriginal.width(), imagenOriginal.height(), opencv_core.IPL_DEPTH_8U, 1);
        opencv_imgproc.cvCvtColor(imagenOriginal, imagenGris, opencv_imgproc.CV_BGR2GRAY);

        // Aplicamos el filtro Canny
        opencv_core.IplImage bordes = opencv_core.IplImage.create(imagenGris.width(), imagenGris.height(), opencv_core.IPL_DEPTH_8U, 1);
        cvCanny(imagenGris, bordes, 100, 200, 3);

        // Mostramos la imagen original y el resultado del procesamiento
        CanvasFrame canvasFrameOriginal = new CanvasFrame("Imagen Original");
        CanvasFrame canvasFrameBordes = new CanvasFrame("Bordes detectados");

        canvasFrameOriginal.setDefaultCloseOperation(javax.swing.JFrame.EXIT_ON_CLOSE);
        canvasFrameBordes.setDefaultCloseOperation(javax.swing.JFrame.EXIT_ON_CLOSE);

        // Mostramos la imagen original
        canvasFrameOriginal.showImage(imagenOriginal);

        // Mostramos el resultado del procesamiento (bordes)
        canvasFrameBordes.showImage(bordes);

        // Liberacion de recursos
        imagenOriginal.release();
        imagenGris.release();
        bordes.release();

        // Esperar hasta que se cierre alguna de las ventanas
        while (canvasFrameOriginal.isVisible() || canvasFrameBordes.isVisible()) {
            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        // Liberar recursos de las ventanas
        canvasFrameOriginal.dispose();
        canvasFrameBordes.dispose();
    }
    
}
