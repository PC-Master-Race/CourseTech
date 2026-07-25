# Lesson images

Put screenshots and other lesson images in this folder.

They are served directly from the site, so no external hosting and no iframe is
needed. Reference one from a lesson like this:

    - type: lesson
      title: Finding the Side Button
      body: |
        Your Side Button is on the right edge.
      images:
        - src: /assets/uploads/side-button.png
          alt: The right edge of an iPhone with the Side Button circled
          caption: The Side Button sits about a third of the way down.

`alt` is required. It is what a screen-reader user hears in place of the picture.
`caption` is optional and prints under the image.

Naming tip: use lowercase words with dashes, like `excel-ribbon-home-tab.png`,
so the files stay easy to find later.
