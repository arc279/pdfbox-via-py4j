package org.kuryu;

import java.io.File;
import java.io.IOException;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;

public class PDFExtractText {
    public static String convert(byte[] input) throws IOException {
        PDDocument doc = PDDocument.load(input);

        PDFTextStripper stripper = new PDFTextStripper();
        String text = stripper.getText(doc);

        doc.close();
        return text;
    }
}

