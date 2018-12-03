package org.interannette;

import org.apache.commons.io.IOUtils;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.BasicCookieStore;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.impl.cookie.BasicClientCookie;

import java.io.IOException;
import java.io.InputStream;

public class InputGetter {


    static String URL_PATTERN = "https://adventofcode.com/2018/day/%s/input";
    static String COOKIE_KEY = "session";

    public static String getInput(int day) throws IOException {
        BasicCookieStore cookieStore = new BasicCookieStore();
        BasicClientCookie cookie = new BasicClientCookie(COOKIE_KEY, getCookieValue());
        cookie.setDomain(".adventofcode.com");
        cookie.setPath("/");
        cookieStore.addCookie(cookie);

        HttpClient client = HttpClientBuilder.create().setDefaultCookieStore(cookieStore).build();

        String url = String.format(URL_PATTERN, day);

        final HttpGet request = new HttpGet(url);

        HttpResponse response = client.execute(request);

        InputStream in = response.getEntity().getContent();
        String body = IOUtils.toString(in, "UTF-8");

        return body;
    }

    private static String getCookieValue() {
        String cookieValue = System.getenv("cookie");
        if(cookieValue == null || cookieValue.isEmpty()) {
            // hacky way to not have to make sure cookie is available in all days.
            throw new RuntimeException("cookie value must be in env properties to use InputGetter.");
        }

        return cookieValue;
    }
}
