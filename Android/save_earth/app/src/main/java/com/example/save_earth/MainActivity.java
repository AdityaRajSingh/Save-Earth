package com.example.save_earth;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

/**
 * Created by root on 20/10/18.
 */

public class MainActivity extends Activity {

    Button reportButton, earthquakeButton, floodButton, cycloneButton, otherButton, helpButton;

    public void onCreate(Bundle savedInstance) {

        super.onCreate(savedInstance);
        setContentView(R.layout.acitivty_main);
        findView();

        reportButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                reportButton.setVisibility(View.INVISIBLE);
                helpButton.setVisibility(View.INVISIBLE);
                earthquakeButton.setVisibility(View.VISIBLE);
                floodButton.setVisibility(View.VISIBLE);
                cycloneButton.setVisibility(View.VISIBLE);
                otherButton.setVisibility(View.VISIBLE);
            }
        });
    }

    public void findView() {
        reportButton = (Button) findViewById(R.id.reportButton);
        earthquakeButton = (Button) findViewById(R.id.earthquakeButton);
        floodButton = (Button) findViewById(R.id.floodButton);
        cycloneButton = (Button) findViewById(R.id.cycloneButton);
        otherButton = (Button) findViewById(R.id.otherButton);
        helpButton = (Button) findViewById(R.id.helpButton);

    }
}
